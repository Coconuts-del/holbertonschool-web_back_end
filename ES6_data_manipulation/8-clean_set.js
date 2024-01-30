export default function cleanSet(set, startString) {
  if (!startString || !startString.length) { return ''; }
  let result = '';
  for (const value of set) {
    if (value.startsWith(startString)) {
      result += `${value.slice(startString.length)}-`;
    }
  }
  if (result.length > 0) { result = result.slice(0, -1); }
  return result;
}
