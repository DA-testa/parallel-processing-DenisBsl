# python3
# 221RDB188 Deniss Buslajevs 8.grupa

def parallel_processing(n, m, data):
    worker = [0] * n

    for i in range(m):
        print(worker.index(min(worker)), min(worker))
        worker[worker.index(min(worker))]+=data[i]
        
    return

def main():
    data = list(map(int, input().split()))
    n = int(data[0])
    m = int(data[1])

    data = list(map(int, input().split()))

    parallel_processing(n,m,data)



if __name__ == "__main__":
    main()
