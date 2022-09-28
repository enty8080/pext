# pext

Pwny dynamic extension.

## Build

```
clang -fPIC -shared pext.c -o pext.so
```

## Usage

While Pwny is running, send command to load custom extension and pass path to the uploaded `pext.so` file to the API call. Pwny will load the library, register extension C2 API calls and let you use them.

Afet that, you can `load pext` in Pwny console and use its features.
