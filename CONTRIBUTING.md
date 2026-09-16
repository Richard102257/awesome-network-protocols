# Contributing

Thank you for improving the protocol map.

## Accepted contributions

- Add a missing protocol or standard.
- Correct a factual error or outdated reference.
- Improve a principle, security note, diagram, or packet example.
- Add an analyzer, simulator, implementation, or teaching resource.
- Translate an existing entry.

## Entry requirements

Every protocol must have a unique lowercase ID, a layer, category, lifecycle status, official standard, HTTPS source, and aligned English and Simplified Chinese metadata.

Use official standards as the primary reference. Secondary tutorials may be added as learning resources, but cannot replace a normative source.

## Workflow

1. Create a focused branch.
2. Edit data/protocols.json and relevant documentation.
3. Run python3 scripts/validate.py from the repository root.
4. Verify all new links manually.
5. Open a pull request and explain the protocol, source, and translation state.

Keep one protocol or one coherent documentation change per pull request when practical.

## Writing style

- Start summaries with what the protocol does.
- Explain the message flow in chronological order.
- Define acronyms on first use.
- State security limits precisely.
- Avoid promotional claims and unsupported performance numbers.
- Mark historic, experimental, and proprietary protocols explicitly.

## Review criteria

Reviewers check source authority, technical accuracy, category fit, translation alignment, link health, licensing, and whether the explanation is understandable without vendor-specific knowledge.

