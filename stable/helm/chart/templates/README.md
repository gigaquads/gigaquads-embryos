# {{ chart.name }}
{{ description }}


## TL;DR;

```console
$ helm install {{ chart.name|dash }}
```

## Installing the Chart

To install the chart with the release name `my-lame-release`:

```console
$ helm install --name my-lame-release stable/{{ chart.name| dash }}
```

## Uninstalling the Chart

To uninstall/delete the `my-lame-release` deployment:

```console
$ helm delete my-lame-release
```

The command removes nearly all the Kubernetes components associated with the
chart and deletes the release.

## Configuration

The following table lists the configurable parameters of this chart and their default values.

| Parameter                   | Description      | Default        |
|-----------------------------|------------------|----------------|
| `path.to.param`             |                  | ``             |
