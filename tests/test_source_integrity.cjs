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
assert(gitignore.split(/\r?\n/).includes('*.csv'), '.gitignore must exclude CSV exports.');
assert(gitignore.split(/\r?\n/).includes('*.xlsx'), '.gitignore must exclude spreadsheet exports.');
assert(!/AIza[0-9A-Za-z_-]{30,}/.test(html), 'Potential Google API key found in the prototype source.');
assert(!/sk-[A-Za-z0-9]{20,}/.test(html), 'Potential API secret found in the prototype source.');
console.log(`Source integrity passed: ${ids.length} unique IDs, ${scripts.length} script block(s), Enter guard, staged hints, and data-export ignore rules.`);
