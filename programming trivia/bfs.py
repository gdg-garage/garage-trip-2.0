import collections


def xxx(root):
    queue = collections.deque([root])
    visited = {root}  # set
    while queue:
        elem = queue.popleft()
        # do something with elem
        for neighbour in elem.children():
            if neighbour in visited:
                continue
            visited.add(neighbour)
            queue.append(neighbour)
