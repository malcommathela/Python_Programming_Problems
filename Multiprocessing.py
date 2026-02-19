from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    print(cpu_count())
    a = Process(target=counter, args=(250000000,))
    a.start()
    a.join()

    b = Process(target=counter, args=(250000000,))
    b.start()
    b.join()

    c = Process(target=counter, args=(250000000,))
    c.start()
    c.join()

    d = Process(target=counter, args=(250000000,))
    d.start()
    d.join()

    print("Finished in: ", time.perf_counter(), "seconds")


if __name__ == '__name__':
    main()
