# Standard library module(s).
import re
from typing import List


def brace_expand(expression: str) -> List[str]:
    """Perform Bash-like brace expansion on the given expression.

    Args:
        expression: The expression to perform the Bash-like brace expansion on.

    Returns:
        The result of the Bash-like brace expansion, in the form of a list of
        strings (rather than just one string, as would be the case in Bash).
    """

    # Tidy up the list by collapsing multiple separators and ensuring we're
    # always comma-separated.
    expression = re.sub("[;,]+", ",", expression)

    # If the expression doesn't have any braces in, add them around the entire
    # expression so that expansion doesn't fail.
    if "{" not in expression:
        expression = f"{{{expression}}}"

    return __expand_lists(__expand_ranges(expression))


def __expand_ranges(expression: str) -> str:
    """Expand ranges in a given expression.

    Args:
        expression: The expression to expand.

    Returns:
        The expression with ranges expanded.
    """

    # Find {n}..{n} in the expression.
    pattern = re.compile("(\\d+)\.\.(\\d+)")

    # Expand ranges
    while True:
        match = pattern.search(expression)
        if match is None:
            break

        left, right = int(match.group(1)), int(match.group(2))
        if left <= right:
            # Replace hyphen expression with comma-separated list.
            numbers = [str(i) for i in range(left, right + 1)]
            expression = expression.replace(match.group(0), ",".join(numbers))

    return expression


def __expand_lists(expression: str) -> List[str]:
    """Expand lists in a given expression.

    Args:
        expression: The expression to expand.

    Returns:
        The lists expanded from the expression.
    """

    # Expand lists.
    results = [expression]
    index = 0
    while index < len(results):
        res = results[index]

        # Find first opening bracket. If there isn't one then we're done.
        open_idx = res.find("{")
        if open_idx == -1:
            index += 1
            continue

        # Find matching closing bracket and extract components. If there's no
        # matching bracket, we're done.
        close_idx = open_idx + 1
        component_idx = close_idx
        level = 0
        components: List[str] = []
        while close_idx != len(res) and not (
            res[close_idx] == "}" and level == 0
        ):
            if res[close_idx] == "{":
                level += 1
            elif res[close_idx] == "}":
                level -= 1
            elif res[close_idx] == "," and level == 0:
                components.append(res[component_idx:close_idx])
                component_idx = close_idx + 1

            close_idx += 1

        if close_idx == len(res):
            index += 1
            continue

        # Add the last component.
        components.append(res[component_idx:close_idx])

        # Add the expanded strings to the results collection, replacing the
        # item that we used to generate them.
        prefix, suffix = res[:open_idx], res[close_idx + 1 :]
        results.pop(index)
        results += [prefix + c + suffix for c in components]

    return results
