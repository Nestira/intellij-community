// "Replace DoubleStream.allMatch(x -> !(...)) with noneMatch(...)" "true"

import java.util.stream.*;

class Test {
  public boolean testAllMatch(double[] data) {
    if(DoubleStream.of(data).noneMatch(d -> Double.isNaN(d)))
      return true;
  }
}