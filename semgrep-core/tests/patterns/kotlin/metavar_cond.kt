class Foo {
    fun foo() {
        x = 1
        // ERROR:
        if (x > 2)
            foo()
    }
}
