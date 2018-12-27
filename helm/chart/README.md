# Helm Chart Embryo


# Converting helm chart to an embryo

The helm chart was created by using `helm` CLI
```
helm create gigaquads
```
then following vim substitution was made, encapsulating Go template syntax delimiters `{{` and `}}` with `{{ '{{' }}`, so that they are not processed by the embryo template erroneously
```
:%s:{{\(\_.\{-}\)\(}}\):{{ '{{' }}\1{{ '}}' }}:g
```
and then converting any reference of `gigaquads` to a jinja varible `{{ name }}` to be processed by embryo, as every helm chart has it's own name and the name can only be specified when calling `helm create` directly
```
:%s:gigaquads:{{ name|dash }}:g
```
