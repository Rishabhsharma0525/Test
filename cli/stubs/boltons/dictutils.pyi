from typing import (
    Any,
    Dict,
    Iterator,
    List,
    Optional,
    Tuple,
    Union,
)

class OneToOne:
    def __delitem__(self, key: int) -> None: ...
    def __init__(self, *a: Any, **kw: Any) -> None: ...
    def __setitem__(
        self, key: Union[str, int], val: Optional[Union[int, str]]
    ) -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> OneToOne: ...
    def pop(self, key: int, default: Any = ...) -> int: ...
    def popitem(self) -> Tuple[int, int]: ...
    def setdefault(self, key: int, default: None = ...) -> None: ...
    def update(self, dict_or_iterable: Dict[int, int], **kw: Any) -> None: ...

class OrderedMultiDict:
    def __delitem__(self, k: str) -> None: ...
    def __eq__(  # type: ignore
        self,
        other: Union[
            Dict[str, int],
            Dict[str, Union[str, Dict[int, int]]],
            Dict[int, int],
            OrderedMultiDict,
        ],
    ) -> bool: ...
    def __getitem__(
        self, k: Union[str, int]
    ) -> Optional[Union[int, str, OrderedMultiDict]]: ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __ne__(self, other: OrderedMultiDict) -> bool: ...  # type: ignore
    def __repr__(self) -> str: ...
    def __reversed__(self) -> Iterator[int]: ...
    def __setitem__(self, k: str, v: Optional[int]) -> None: ...
    def _clear_ll(self) -> None: ...
    def _insert(
        self,
        k: Union[str, int],
        v: Optional[Union[int, OrderedMultiDict, str]],
    ) -> None: ...
    def _remove(self, k: str) -> None: ...
    def _remove_all(self, k: str) -> None: ...
    def add(
        self,
        k: Union[str, int],
        v: Optional[Union[str, int, OrderedMultiDict]],
    ) -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> OrderedMultiDict: ...
    def getlist(self, k: str, default: Any = ...) -> Union[List[int], List[str]]: ...
    def inverted(self) -> OrderedMultiDict: ...
    def items(
        self, multi: bool = ...
    ) -> Union[List[Tuple[str, int]], List[Tuple[str, str]], List[Tuple[int, str]]]: ...
    def iteritems(
        self, multi: bool = ...
    ) -> Iterator[
        Union[
            Tuple[int, int],
            Tuple[str, None],
            Tuple[str, str],
            Tuple[str, int],
            Tuple[int, str],
        ]
    ]: ...
    def iterkeys(self, multi: bool = ...) -> Iterator[Union[str, int]]: ...
    def itervalues(self, multi: bool = ...) -> Iterator[Union[str, int]]: ...
    def keys(self, multi: bool = ...) -> Union[List[int], List[str]]: ...
    def pop(self, k: str, default: Any = ...) -> Union[str, int]: ...
    def popall(
        self, k: str, default: Any = ...
    ) -> Optional[Union[List[int], List[str]]]: ...
    def poplast(self, k: Any = ..., default: Any = ...) -> Union[str, int]: ...
    def setdefault(self, k: str, default: Any = ...) -> None: ...
    def todict(self, multi: bool = ...) -> Dict[str, Union[int, str]]: ...
    def update(
        self,
        E: Union[
            List[Tuple[int, int]],
            List[Union[Tuple[str, OrderedMultiDict], Tuple[str, str]]],
            OrderedMultiDict,
        ],
        **F: Any,
    ) -> None: ...
    def update_extend(self, E: Any, **F: Any) -> None: ...
    def values(self, multi: bool = ...) -> Union[List[int], List[str]]: ...
