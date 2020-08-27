# Test project

This is a test project to test relative-link-corrector. 

The expected functionality is to convert the `md` extension of files to `html`
in relative links, but not in any other case. 

- [link 1](linked.md) should be converted
- [link 2](linked.md#anchor) should be corrected
- [link 3](https://github.com/cntt-n/relative-link-corrector/linked.md) should not be corrected
- [link 4](https://github.com/cntt-n/relative-link-corrector/linked.md#anchor) should not be corrected

