# Examples: Code Readability Best Practices

---

## Example 1: Reordering functions for top-down flow

### Before (without this skill)

```js
function formatDate(dateString) {
  return new Date(dateString).toLocaleDateString();
}

function saveReport(reportText) {
  // save to database
}

function processUserReport(userId) {
  const rawData = fetchUserData(userId);
  const report = buildReport(rawData);
  saveReport(report);
}

function buildReport(data) {
  const cleanDate = formatDate(data.date);
  const cleanScore = formatScore(data.score);
  return data.name + ': ' + cleanScore + ' ' + cleanDate;
}
```

### After (with this skill applied)

```js
function processUserReport(userId) {
  const rawData = fetchUserData(userId);
  const report = buildReport(rawData);
  saveReport(report);
}

function fetchUserData(userId) {
  // get data from the database
}

function buildReport(data) {
  const cleanDate = formatDate(data.date);
  const cleanScore = formatScore(data.score);
  return data.name + ': ' + cleanScore + ' ' + cleanDate;
}

function saveReport(reportText) {
  // save to the database
}

function formatDate(dateString) {
  return new Date(dateString).toLocaleDateString();
}

function formatScore(number) {
  return number.toFixed(1);
}
```

### Why it's better

The file starts with the headline. The call flow moves downward, and shared formatting helpers are grouped together lower in the file.

---

## Example 2: Replacing vague comments with actionable TODOs

### Before (without this skill)

```js
// might break on slow server
// not sure if this works for edge case
if (user.id) {
  loadData(user.id);
}
```

### After (with this skill applied)

```js
// TODO: Add a timeout guard here.
// If the server response exceeds 5 seconds,
// the UI can freeze during load.
if (user.id) {
  loadData(user.id);
}
```

### Why it's better

The improved comment names the real condition, describes the impact, and suggests the next action.

---

## Example 3: Removing noise from obvious code

### Before (without this skill)

```js
// This function uses the Base64 encoding standard defined in RFC 4648...
function encodeImage(data) {
  return Buffer.from(data).toString('base64');
}
```

### After (with this skill applied)

```js
function encodeImage(data) {
  return Buffer.from(data).toString('base64');
}
```

### Why it's better

The code is already self-explanatory. The deleted comment added noise, not clarity.

---

## Example 4: Converting markup-heavy comments to plain text

### Before (without this skill)

```js
// <p>Calculates the <b>final price</b> for cart items.</p>
// <ul><li>Applies seasonal discounts</li><li>Adds tax</li></ul>
function calculateFinalPrice(items) {
  // ...
}
```

### After (with this skill applied)

```js
// Calculates the final price for cart items.
// Applies seasonal discounts and region-based tax.
function calculateFinalPrice(items) {
  // ...
}
```

### Why it's better

The revised comment is readable in any editor, avoids visual markup noise, and keeps the useful meaning while reducing clutter.

