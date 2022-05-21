class WearyArrayTraveler:
    def can_move_forward(self,array,idx, used_indexs):
        new_idx = idx + array[idx]
        return (new_idx,new_idx <= len(array) - 1 and new_idx not in used_indexs)

    def can_move_backward(self,array,idx, used_indexs):
        new_idx = idx - array[idx]
        return (new_idx,idx>0 and new_idx >= 0 and new_idx not in used_indexs)


    def is_array_traversable(self, array):
        if(not isinstance(array,list)):
            return False

        if(len(array)==0):
            print("Can't traverse a zero length array")
            return False

        if(len(array)==1):
            return True

        try:
            LAST_ELEMNT_IDX = len(array) - 1
            dfs_stack = []
            dfs_stack.append(0)

            used_indexs = set()

            while (len(dfs_stack) > 0):
                idx = dfs_stack.pop()
                if (idx == LAST_ELEMNT_IDX):
                    return True

                if array[idx]<0:
                    print("Can't except negative values")
                    return False

                newIdxFwrd,canMoveForward=self.can_move_forward(array,idx,used_indexs)
                if (canMoveForward):
                    used_indexs.add(newIdxFwrd)
                    dfs_stack.append(newIdxFwrd)

                newIdxBkwrd,canMoveBackward=self.can_move_backward(array,idx,used_indexs)
                if(canMoveBackward):
                    used_indexs.add(newIdxBkwrd)
                    dfs_stack.append(newIdxBkwrd)
            return False
        except Exception as ex:
            print("Error: "+ex)
            return False


if __name__ == '__main__':
    myArrayTraveler= WearyArrayTraveler()
    print(myArrayTraveler.is_array_traversable([4, 4, 1, 1, 2, 2, 1000, 1]))

