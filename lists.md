# Quick list creation

## Homogeneous list of size `n`
```python
l = [0] * n
```
*Make sure that the seed is immutable*

## List of size `n` of 0..`n`
```python
l = list(range(n))
```

## Heterogeneous list of size `n`
```python
l = [0] * n
for i in range(n):
  l[i] = ...
```

## Mapping a list `l` with function `f`
```python
new_l = list(map(f, l))
```