#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints info on a pyobject
 * @p: python object
 */
void print_python_list_info(PyObject *p);

void print_python_list_info(PyObject *p)
{
	int size, real, i;
	PyObject *temp;
	Py_ssize_t allocated;

	size = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %zd\n", allocated);
	real = PyList_check(p);
	if (reak)
	{
		for (i = 0; i < size; i++)
		{
			temp = PyList_getItem(p, i);
			printf("Element %d: %s\n", i, Py_TYPE(temp)->tp_name);
		}
	}
}
