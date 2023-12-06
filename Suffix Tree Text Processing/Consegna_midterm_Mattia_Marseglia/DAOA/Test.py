from DNAContamination import DNAContamination
from TdP_collections.priority_queue.heap_priority_queue import HeapPriorityQueue

""" this function reads DNA strings from the dataset target_batcha.fasta and returns the indices of the k contaminants 
    in the dataset with larger degree of contamination in s, assuming l as contamination threshold.
    Specifically, the function return a string containing these indices in increasing order
    separated by comma."""
def test(s, k, i):
    d = DNAContamination(s, i)
    f = open("target_batch.fasta", "r")
    index = f.readline()[1:-1]
    contaminant = f.readline()[:-1]
    tmp_map = {}
    while index != "" and contaminant != "":
        tmp_map[contaminant] = int(index)
        d.addContaminant(contaminant)
        index = f.readline()[1:-1]
        contaminant = f.readline()[:-1]
    f.close()
    tuple_list = d.getContaminants(k)
    tmp_queue = HeapPriorityQueue()
    for elem in tuple_list:
        tmp_queue.add(tmp_map.get(elem), elem)
    """build the string to return:"""
    str_to_ret = ""
    if not tmp_queue.is_empty():
        str_to_ret = tmp_queue.remove_min()[0].__str__()
    while not tmp_queue.is_empty():
        str_to_ret += ", " + tmp_queue.remove_min()[0].__str__()
    return str_to_ret