using System;

public interface Maybe<T>{}

public class Nothing<T> : Maybe<T>
{
    public override string ToString()
    {
        return "Nothing";
    }
}

public class Something<T> : Maybe<T>
{
    public T Value { get; private set; }
    public Something (T value)
    {
        Value = value;
    }
    public override string ToString()
    {
        return Value.ToString();
    }
}

public static class MaybeMonad 
{
  public static Maybe<T> ToMaybe<T>(this T value)
  {
	  return new Something<T>(value);
  }

  public static Maybe<B> Bind<A, B>(this Maybe<A> a, 
    				    Func<A, Maybe<B>> func)
  {
    var something = a as Something<A>;
    return something == null ? 
        		  new Nothing<B>() : 
		         func(something.Value);
  }
}

public static class Extensions
{
  public static Maybe<int> Div(this int numerator, int denominator)
  {
    return denominator == 0
               ? (Maybe<int>)new Nothing<int>()
               : new Something<int>(numerator/denominator);
  }
}

class MainClass {
  public static void Main (string[] args) {
    Console.WriteLine (3.ToMaybe());
    Console.WriteLine ("Hello World".ToMaybe());
    Console.WriteLine (15.Div(3));
    Console.WriteLine (15.Div(3).Bind(n => Extensions.Div(n, 0)));
    Console.WriteLine (36.ToMaybe().Bind(n => Extensions.Div(n, 3)).Bind(m => Extensions.Div(m, 0)).Bind(p => Extensions.Div(p, 9)));
  }
}