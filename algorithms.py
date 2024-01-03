from main import draw_list

#Algorithms

def bubble_sort(draw_info,ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            num1 = lst[j]
            num2 = lst[j+1]
            
            if (num1>num2 and ascending) or (num1<num2 and not ascending):
                lst[j],lst[j+1] = lst[j+1],lst[j]
                draw_list(draw_info,{j:(255,0,0),j+1:(0,255,0)})
                yield True
    return lst


def insertion_sort(draw_info,ascending=True):
	lst = draw_info.lst

	for i in range(1, len(lst)):
		current = lst[i]

		while True:
			ascending_sort = i > 0 and lst[i - 1] > current and ascending
			descending_sort = i > 0 and lst[i - 1] < current and not ascending

			if not ascending_sort and not descending_sort:
				break

			lst[i] = lst[i - 1]
			i = i - 1
			lst[i] = current
			draw_list(draw_info, {i - 1: (0,255,0), i: (255,0,0)})
			yield True

	return lst


def selection_sort(draw_info,ascending=True):
    lst = draw_info.lst
    size = len(lst)
    for s in range(size):
        min_idx = s
         
        for i in range(s + 1, size):
            if lst[i] > lst[min_idx] and not ascending:
                min_idx = i
            if lst[i] < lst[min_idx] and ascending:
                min_idx = i


        (lst[s], lst[min_idx]) = (lst[min_idx], lst[s])
        draw_list(draw_info,{s:(255,0,0),min_idx:(0,255,0)})
        yield True
    
    return lst


def shell_sort(draw_info,ascending=True):
    lst = draw_info.lst
    n = len(lst)
    gap=n//2
            
    while gap>0:
        j=gap
        while j<n:
            i=j-gap
              
            while i>=0:
                if (lst[i+gap]>lst[i] and ascending) or (lst[i+gap]<lst[i] and not ascending):
                    break
                else:
                    lst[i+gap],lst[i]=lst[i],lst[i+gap]
                    draw_list(draw_info,{i:(255,0,0),i+gap:(0,255,0)})
                    yield True

                i=i-gap
            j+=1
        gap=gap//2


def cocktail_sort(draw_info,ascending=True):
    lst = draw_info.lst
    n = len(lst)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):
        swapped = False

        for i in range(start, end):
            if (lst[i] > lst[i + 1] and ascending):
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
                draw_list(draw_info,{i:(255,0,0),i+1:(0,255,0)})
                yield True
            elif (lst[i] < lst[i + 1] and not ascending):
                lst[i+1], lst[i] = lst[i], lst[i+1]
                swapped = True
                draw_list(draw_info,{i:(255,0,0),i+1:(0,255,0)})
                yield True
        if (swapped == False):
            break
 
        swapped = False
 
        end = end-1
 
        for i in range(end-1, start-1, -1):
            if (lst[i] > lst[i + 1] and ascending):
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
            elif (lst[i] < lst[i + 1] and not ascending):
                lst[i+1], lst[i] = lst[i], lst[i+1]
                swapped = True
        start = start + 1