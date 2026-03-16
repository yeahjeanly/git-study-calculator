def divide(a, b):
    if b == 0:
        return "0으로 나눠 수 없습니다"
    return a / b

def main():
    print("=== 계산기 프로그램 ===")
    result = divide(10, 2)
    print(f"10 / 2 = {result}")

if __name__ == "__main__":
    main()
    