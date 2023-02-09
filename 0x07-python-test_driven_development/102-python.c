#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p)
{
    if (!PyUnicode_Check(p))
    {
        fprintf(stderr, "Error: Not a valid Python string\n");
        return;
    }

    PyObject *encoded_str = PyUnicode_AsEncodedString(p, "utf-8", "strict");
    if (encoded_str == NULL)
    {
        fprintf(stderr, "Error: Failed to encode the Python string\n");
        return;
    }

    char *c_str = PyBytes_AsString(encoded_str);
    printf("%s\n", c_str);

    Py_DECREF(encoded_str);
}

