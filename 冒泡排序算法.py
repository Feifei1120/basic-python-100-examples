#所谓冒泡，就是将元素两两之间进行比较，谁大就往后移动， 直到将最大的元素排到最后面， 接着再循环一趟， 从头开始进行两两比较， 而上一趟已经
#排好的元素就不用进行比较了

def bubble_sort(items):
    for i in range(len(items)-1):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items

list = [2,9,15,31,120,45,6,85,17]
print(bubble_sort(list))