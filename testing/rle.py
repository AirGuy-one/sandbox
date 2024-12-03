def rle_encode(input_string: str) -> str:
    if not input_string:
        return ""

    result = []
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            result.append(str(count) + input_string[i - 1])
            count = 1
    result.append(str(count) + input_string[-1])  # Добавить последний символ
    return ''.join(result)


input_string = "AAAABBBCCDAA"
encoded_string = rle_encode(input_string)
print(f"Encoded: {encoded_string}")
