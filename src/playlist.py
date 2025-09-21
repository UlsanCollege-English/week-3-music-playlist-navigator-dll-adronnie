class _DNode:
    __slots__ = ("title", "prev", "next")

    def __init__(self, title):
        self.title = title
        self.prev = None
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, title):
        """Append song at the end of the playlist"""
        node = _DNode(title)
        if not self.head:  # first song
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        return True

    def play_first(self):
        """Move to the first song and return its title"""
        if not self.head:
            return None
        self.current = self.head
        return self.current.title

    def next(self):
        """Move to the next song if possible, else stay at tail"""
        if not self.current:
            return None
        if self.current.next:
            self.current = self.current.next
        return self.current.title

    def prev(self):
        """Move to the previous song if possible, else stay at head"""
        if not self.current:
            return None
        if self.current.prev:
            self.current = self.current.prev
        return self.current.title

    def insert_after_current(self, title):
        """Insert a new song right after the current one"""
        if not self.current:  # empty playlist
            return self.add_song(title)

        node = _DNode(title)
        nxt = self.current.next

        # link new node
        self.current.next = node
        node.prev = self.current
        node.next = nxt

        if nxt:
            nxt.prev = node
        else:
            self.tail = node  # inserting at the end
        return True

    def remove_current(self):
        """Remove the current song and move cursor appropriately"""
        if not self.current:
            return False

        node = self.current

        # Fix head/tail
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        # Move current
        if node.next:
            self.current = node.next
        elif node.prev:
            self.current = node.prev
        else:
            self.current = None  # playlist empty

        return True

    def to_list(self):
        """Return all song titles as a Python list"""
        res = []
        node = self.head
        while node:
            res.append(node.title)
            node = node.next
        return res
