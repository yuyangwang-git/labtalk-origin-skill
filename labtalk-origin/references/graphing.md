# Graphing

Use this reference for plotting worksheet data, editing graph layers, axes, and graphical objects.

## Basic Plotting

```labtalk
// Select a Y column first, or pass explicit ranges.
plotxy;

plotxy iy:=col(2) plot:=202 color:=1;
plotxy iy:=rResult plot:=202 color:=2 size:=1 ogl:=1;
```

- `plotxy` creates or adds XY plots.
- `iy` is the input Y range; X is often inferred from worksheet designation.
- Use `ogl:=1` to plot into the active graph layer.

## Axis And Layer Properties

```labtalk
layer.x.from = 5;
layer.x.to = 100;
layer.y.type = 2;
```

- `layer` refers to the active graph layer.
- Use explicit graph/layer references when editing a non-active graph.

## Graphical Objects

```labtalk
label -s -n myLabel "Peak A";
myLabel.x = 50;
myLabel.y = 10;
```

Graphical objects include labels, arrows, lines, and other user-created graph/page elements.

## Exporting Graphs

For graph export patterns, read `references/importing-exporting.md`; common X-Functions include `expGraph` and related export tools.
