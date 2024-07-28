# Input elements for the lists
ip1 = input("Enter the elements in list1 (space-separated): ").split()
ip2 = input("Enter the elements in list2 (space-separated): ").split()
ip1.append("Avi")
print("After appending 'Avi':", ip1)
ip1.insert(1, "JAY")
print("After inserting 'JAY':", ip1)
ip1.extend(ip2)
print("After appending ip2:", ip1)
ip1.pop(1)
print("After popping element at index 1:", ip1)
try:
    ip1.remove("avi")
except ValueError:
    print("'avi' not found in the list")
print("After removing 'avi':", ip1)
ip1.sort()
print("Sorted in ascending order:", ip1)
ip1.sort(reverse=True)
print("Sorted in descending order:", ip1)
