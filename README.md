# claude-code-guide-practice

Claude Code 가이드 실습용 프로젝트입니다.

## Functions

### `add(a: int, b: int) -> int`

두 정수를 더한 결과를 반환합니다.

```python
from ex_pipeline import add

add(1, 2)   # 3
add(-1, 1)  # 0
```

### `divide(a: int, b: int) -> float`

두 정수를 나눈 결과를 `float`로 반환합니다. `b`가 0이면 `ZeroDivisionError`를 발생시킵니다.

```python
from ex_pipeline import divide

divide(10, 2)  # 5.0
divide(7, 2)   # 3.5
divide(1, 0)   # raises ZeroDivisionError: Cannot divide by zero
```
