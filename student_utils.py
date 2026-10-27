def parse_student(line):
    parts = line.strip().split(",")
    if len(parts) != 2:
        raise ValueError(f"字段数量不为 2（当前 {len(parts)} 个字段）")
    name, score_str = parts
    if name == "":
        raise ValueError("姓名为空")
    try:
        score = int(score_str)
    except ValueError:
        raise ValueError(f"成绩 '{score_str}' 不是整数") from None
    if not (0 <= score <= 100):
        raise ValueError(f"成绩 {score} 超出 0~100 范围")
    return name, score
