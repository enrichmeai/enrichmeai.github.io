import { Parser } from '@asyncapi/parser';
import fs from 'fs';
const p = new Parser();
const { document, diagnostics } = await p.parse(fs.readFileSync(process.argv[2], 'utf8'));
const errs = diagnostics.filter(d => d.severity === 0);
console.log(document ? 'valid' : 'INVALID', 'errors:', errs.length, 'warnings:', diagnostics.length - errs.length);
for (const d of diagnostics) console.log(d.severity, d.code, d.message);
process.exit(document && errs.length === 0 ? 0 : 1);
