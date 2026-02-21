SOLANA_REFACTOR_PROMPT = """
You are a Senior Solana Program Architect. Refactor the following Anchor (Rust) code.
Your goal is to minimize Compute Units (CU) and ensure strict account safety.

### Optimization Rules:
1. **CU Efficiency**: Use `#[inline(always)]` for small helper functions.
2. **Memory Management**: If structs are large, suggest `Box<T>` to avoid stack overflows.
3. **Lazy Loading**: Use `LazyAccount<'info, T>` for large accounts where only specific fields are read.
4. **Serialization**: Use `#[account(zero_copy)]` for accounts exceeding 1KB.
5. **PDA Safety**: Ensure `bump` seeds are stored and validated with `has_one`.
6. **Bitwise Logic**: Replace expensive division/multiplication with bit-shifting where applicable.

### Input Code:
{code}

### Detected Issues:
{issues}

Return ONLY the refactored Rust code inside a ```rust block.
"""
