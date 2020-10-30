from .help import dp
from .start import dp
from .testing import dp
from .admin import dp
# echo перезватывает все текстовые сообщения
# и если поместить выше старта то старт не выполнится никогда
from .echo import dp
# порядок важен!
__all__ = ["dp"]
