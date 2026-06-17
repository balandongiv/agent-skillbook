# Examples: Citation Relevance Audit

## Example 1: Catching a partially-supporting citation

### Before (without this skill)

```
Blinking can be influenced by both physiological and cognitive factors \citep{nystrm2024what,nystrm2030paper}.
```

Both citations are assumed to support the whole sentence.

### After (with this skill applied)

```json
{
  "synthesized_statement": "Blinking can be influenced by both physiological and cognitive factors \\citep{nystrm2024what,nystrm2030paper}.",
  "sources": [
    { "citing_key": "nystrm2024what", "actual_text": "Blinking is associated with eyelid closure and reopening." },
    { "citing_key": "nystrm2030paper", "actual_text": "Blinking may vary according to cognitive and physiological conditions." }
  ],
  "relevance_assessment": "Partially relevant",
  "notes": "nystrm2024what supports the physiological definition but not the cognitive-factor claim; nystrm2030paper supports the cognitive/physiological-factor claim. Reassign nystrm2024what or drop it from this sentence."
}
```

### Why it's better

The audit shows exactly which source supports which atomic claim and recommends a concrete fix, instead
of assuming both citations cover everything.

---

## Example 2: Removing an irrelevant (topical-but-wrong) citation

### Before (without this skill)

```
Amplitude thresholding localizes blink peaks \citep{somefatiguepaper2019}.
```

`somefatiguepaper2019` is about drowsiness classification, not peak localization.

### After (with this skill applied)

```json
{
  "synthesized_statement": "Amplitude thresholding localizes blink peaks \\citep{somefatiguepaper2019}.",
  "sources": [
    { "citing_key": "somefatiguepaper2019", "actual_text": "We classify drowsiness levels from EEG band power features." }
  ],
  "relevance_assessment": "Not relevant",
  "notes": "Source is about drowsiness classification, not amplitude-threshold peak localization. Remove this citation and replace with a thresholding/peak-detection reference."
}
```

### Why it's better

A same-domain but non-supporting citation is identified by its actual text and removed/flagged, rather
than passing review because the topic looked related.
