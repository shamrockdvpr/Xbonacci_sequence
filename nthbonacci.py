def nthbonacci(signature, n):
    seq = [0] * n
    if n < len(signature):
        seq[0:n] = signature
        print(seq[0:n])
        return seq[0:n]
    seq[0:len(signature)] = signature

    for index in range(len(signature), n):
        seq[index] = (sum(seq[index - len(signature): index]))

    return seq
