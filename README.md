# workstation-disk-encryption-checker

Check disk encryption per workstation: encrypted with a named method, encrypted with no method recorded, or not encrypted — unencrypted machines first.

## How to run

```sh
python3 main.py workstations.csv
```

## Example output

```
PC-12: NOT ENCRYPTED (-)
PC-07: ENCRYPTED (BitLocker)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
