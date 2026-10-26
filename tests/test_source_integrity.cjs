const fs = require('fs');
const path = require('path');
const os = require('os');
const { execFileSync } = require('child_process');

const root = path.resolve(__dirname, '..');
const htmlPath = path.join(root, 'index.html');
const html = fs.readFileSync(htmlPath, 'utf8');
const gitignore = fs.readFileSync(path.join(root, '.gitignore'), 'utf8');

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

const ids = [...html.matchAll(/\bid=["']([^"']+)["']/g)].map(m => m[1]);
const duplicates = ids.filter((id, index) => ids.indexOf(id) !== index);
assert(duplicates.length === 0, `Duplicate IDs found: ${[...new Set(duplicates)].join(', ')}`);

const scripts = [...html.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/gi)].map(m => m[1]);
assert(scripts.length > 0, 'No inline JavaScript was found.');
const temp = path.join(os.tmpdir(), `frameshift-check-${process.pid}.js`);
fs.writeFileSync(temp, scripts.join('\n;\n'), 'utf8');
try {
  execFileSync(process.execPath, ['--check', temp], { stdio: 'pipe' });
} finally {
  try { fs.unlinkSync(temp); } catch (_) {}
}

assert(html.includes("if(e.key==='Enter'&&(e.target?.closest?.('button')||document.activeElement?.closest?.('button')))return;"),
  'Global Enter handler is missing the native-button guard.');
assert(html.includes('function progressiveDILRHint(key)'), 'Progressive DILR hint function is missing.');
assert(html.includes('record.coachHintStages={...coachHintStages}'), 'Coach hint stage is not included in local session state.');
assert(html.includes("const SESSION_STORAGE_KEY='frameshift-session-v10'"), 'Session storage key/version is missing.');
assert(html.includes('function persistSessionState()') && html.includes('function restoreSavedSession()'), 'Session save/restore functions are missing.');
assert(html.includes('id=\"resumeSessionBtn\"') && html.includes('id=\"discardSessionBtn\"'), 'Resume/discard controls are missing.');
assert(!html.includes("$('q1Tita').addEventListener('keydown'"), 'Q1 TITA must not auto-submit on Enter.');
assert(!html.includes("$('q2Tita').addEventListener('keydown'"), 'Q2 TITA must not auto-submit on Enter.');
assert(html.includes('aria-hidden=\"true\" focusable=\"false\">${grid.join'), 'Visual SVG must be hidden from assistive tech when equivalent table is exposed.');
assert(html.includes('<details class=\"chart-data-wrap\" open>'), 'Accessible chart data table must be open by default.');
assert(gitignore.split(/\r?\n/).includes('*.csv'), '.gitignore must exclude CSV exports.');
assert(gitignore.split(/\r?\n/).includes('*.xlsx'), '.gitignore must exclude spreadsheet exports.');
assert(!/AIza[0-9A-Za-z_-]{30,}/.test(html), 'Potential Google API key found in the prototype source.');
assert(!/sk-[A-Za-z0-9]{20,}/.test(html), 'Potential API secret found in the prototype source.');
console.log(`Source integrity passed: ${ids.length} unique IDs, ${scripts.length} script block(s), session recovery, TITA submission guards, chart-table accessibility and export ignore rules.`);
