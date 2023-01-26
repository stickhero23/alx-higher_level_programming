#include <Python.h>
/**
 * print_python_list - function to print lists
 * @p: pointer to list
 * Return: prints the list or Error
 */
void print_python_list(PyObject *p)
{
	/* check if object is a list */
	if (!PyList_Check(p))
	{
		printf("Error: Invalid PyListObject\n");
		return;
	}
	Py_ssize_t size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}

}
/**
 * print_python_bytes - function to print bytes
 * @p: pointer to the bytes
 * Return: print error if not byte else print byte
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("Error: Invalid PyBytesObject\n");
		return;
	}
	Py_ssize_t size = PyBytes_Size(p);

	printf("[*] Python bytes info\n");
	printf("[*] Size of the Python Bytes = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyVarObject *)p)->ob_size);
	printf("First %ld bytes: ", size < 10 ? size : 10);

	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
		printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
	}
	printf("\n");
}
/**
 * print_python_float - function to print float
 * @p: pointer
 * Return: print float else print error
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("Error: Invalid PyFloatObject\n");
		return;
	}
	double value = PyFloat_AS_DOUBLE(p);

	printf("[*] Python float info\n");
	printf("[*] Value: %f\n", value);
}

