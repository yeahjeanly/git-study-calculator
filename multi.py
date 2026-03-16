history = []

def add(a, b):                                       # ← 참여자 1과 충돌!
    result = a + b
    history.append(f"{a} + {b} = {result}")
    return result

def subtract(a, b):                                  # ← 참여자 2와 충돌!
    result = a - b
    history.append(f"{a} - {b} = {result}")
    return result

def show_history():
    print("=== 계산 기록 ===")
    for h in history:
        print(h)

def main():                                          # ← main()도 충돌!
    print("=== 계산기 프로그램 ===")
    add(10, 5)
    subtract(10, 3)
    show_history()

if __name__ == "__main__":
    main()