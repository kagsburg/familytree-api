



def ancestorEntity( self, entity, ancestor ):
    """Returns the ancestor entity of the given entity.
    """
    if entity is None:
        return None
    if entity == ancestor:
        return entity
    for parent in entity.parents:
        if parent == ancestor:
            return parent
        else:
            return self.ancestorEntity( parent, ancestor )
    return None
def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}
def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
