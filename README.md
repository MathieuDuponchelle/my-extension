# Build

python3 setup.py bdist_egg

# Test

```
cd /path/to/hotdoc/documentation
hotdoc run --extra-extension-path=/path/to/my-extension
```

Should print

```
Setting up
```

With no-pkg-resources prints:

```
WARNING: [core]: (extension-import): Failed to load EntryPoint(name='get_extension_classes', value='my_extension.my_extension:get_extension_classes', group='hotdoc.extensions') No module named 'my_extension'
```
