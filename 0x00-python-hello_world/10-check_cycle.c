#include "lists.h"
/**
 * check_cycle - a function that checks if a singly linked list has a cycle in it
 * list: linked list
 * Return: 1 if there is a cycle, otherwise return 0
 */
int check_cycle(listint_t *list)
{
	listint_t *f, *s;

	if (!list || !list->next)
		return (0);
	f = list;
	s = list;

	while (s != NULL && f != NULL && f->next != NULL)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
		{
		return (1);
		}
	}
	return (0);
}
