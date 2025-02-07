
  def branch(self,index):
    """_summary_

    Args:
        index (int): integer specifying where memory should branch
    """
    self.cr = index
    print("You have branched to location" + str(index))

  def branchneg(self,index):
    """_summary_
      If accumulator is negative branch to a specific location
    """
    if self.accumulator < 0:
      self.branch(index)
    else:
      print("Accumulator isn't negative, there was no branching ")

  def branchzero(self,index):
    """_summary_

      If accumulator is zero branch to a specific location
    """
    if self.accumulator == 0:
      self.branch(index)
    else:
        print("Accumulator isn't zero, there was no branching ")
