
#constant

number_of_queries, query_length, base_string_length = 0

decimal = 256

prime_number = 1117

base_string, query = ""

hashes, queries = []






#functions
def hash_function(text: str) -> None:

    total_hash = 0
    hash = 0

    for i in range(query_length-1):
        hash = (hash * decimal) % prime_number

    for i in range(query_length):
        total_hash = (decimal * total_hash + text[i]) % prime_number

    hashes.append(total_hash)

    for i in range(base_string_length - query_length + 1):
        total_hash = (
            decimal * (total_hash - text[i] * hash) + text[i+query_length]) % prime_number

        if (total_hash < 0):
            total_hash += prime_number
        hashes.append(total_hash)


def does_dataset_have(query: str) -> int:
    local_hash = 0

    for i in range(query_length):
        local_hash = (decimal * local_hash + query[i]) % prime_number

    for i in range(len(hashes)):
        if(local_hash == hashes[i]):
            for j in range(query_length):
                if (base_string[i+j] != query[j]):
                    break
            if(j == query_length):
                return i
    return -1


def main():

    #inputs
    base_string = input()
    number_of_queries = int(input())
    query_length = int(input())
    base_string_length = len(base_string)


    queries = [input() for i in range(number_of_queries+1)]

    hash_function(base_string)

    for i in number_of_queries + 1:
        query = queries[i]
        index = does_dataset_have(query)
        if (index != -1):
            print(f"The sequence: {query} found at the position: {index + 1} \n")
        
        else:
            print(f"The sequence: {query} found at the position: {index + 1} \n")


if __name__ == "__main__":
    main()




