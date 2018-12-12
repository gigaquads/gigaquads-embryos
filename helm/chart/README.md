

The following vim substitution will handle encapsulating Go template syntax delimiters `{{` and `}}`, such as `{{ '{{' }}`
```
:%s:{{\(\_.\{-}\)\(}}\):{{ '{{' }}\1{{ '}}' }}:g
```
