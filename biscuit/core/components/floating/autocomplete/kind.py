from __future__ import annotations

import typing

from biscuit.core.components.utils.icon import Icon

from .kinds import kinds

if typing.TYPE_CHECKING:
    from .item import CompletionItem


class Kind(Icon):
    def __init__(self, master: CompletionItem, kind: int=1, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.base = master.base

        self.config(**self.base.theme.editors.autocomplete.item)
        self.set_kind(kind)

    def set_kind(self, kind: int=1):
        if not kind:
            return
        
        self.set_icon(kinds[kind-1])
