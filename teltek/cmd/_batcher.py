import logging
from collections.abc import Iterable, Iterator
from functools import cache

import teltek.parameters

_LOGGER = logging.getLogger(__name__)


def iter_param_batches(
    param_ids: Iterable[int], max_command_len: int
) -> Iterator[list[int]]:
    batch: list[int] = []
    batch_len = 0

    # the response is always longer
    resp_overhead_len = len("Param ID: Value:")
    max_len_map = _id_to_max_len_map()

    param_ids = iter(param_ids)
    while True:
        try:
            param_id = next(param_ids)
        except StopIteration:
            if batch:
                yield batch
            break

        max_len = max_len_map[param_id]
        # for every parameter we add ";{id}:{value}"
        additional_len_required = len(f";{param_id}:") + max_len

        if resp_overhead_len + batch_len + additional_len_required > max_command_len:
            # no more room in current batch
            if batch:
                yield batch
            else:
                _LOGGER.warning(
                    "parameter %s itself exceeds max_command_len (%s > %s), returning on its own",
                    param_id,
                    additional_len_required,
                    max_command_len,
                )
                yield [param_id]
            # start new batch
            batch = [param_id]
            batch_len = additional_len_required
        else:
            # add to current batch
            batch.append(param_id)
            batch_len += additional_len_required


@cache
def _id_to_max_len_map() -> dict[int, int]:
    id_to_len: dict[int, int] = {}
    for param in teltek.parameters.db.iter_parameters():
        max_len = param.max_raw_len()
        for id in param.iter_ids():
            id_to_len[id] = max_len
    return id_to_len
