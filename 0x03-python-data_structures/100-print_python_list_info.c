#include <Python.h>

/**
 * print_python_list_info - function to print basic info about Python lists
 * @p: input
 * 
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	size_t length = PyList_Size(p);

	printf("[*] Size of the Python list = %d\n", length);
	printf("[*] Allocated = %d\n", object->allocated);
	for (i = 0, i < length; i++)
	{
		printf("Element %d: %s\n", i, "str");
	}
}
