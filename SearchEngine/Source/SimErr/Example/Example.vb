Imports Microsoft.VisualStudio.TestTools.UnitTesting

Imports SimErr



'''<summary>
'''This is a test class for SimErrTest and is intended
'''to contain all SimErrTest Unit Tests
'''</summary>
<TestClass()> _
Public Class Example


    Private testContextInstance As TestContext

    '''<summary>
    '''Gets or sets the test context which provides
    '''information about and functionality for the current test run.
    '''</summary>
    Public Property TestContext() As TestContext
        Get
            Return testContextInstance
        End Get
        Set(value As TestContext)
            testContextInstance = Value
        End Set
    End Property

#Region "Additional test attributes"
    '
    'You can use the following additional attributes as you write your tests:
    '
    'Use ClassInitialize to run code before running the first test in the class
    '<ClassInitialize()>  _
    'Public Shared Sub MyClassInitialize(ByVal testContext As TestContext)
    'End Sub
    '
    'Use ClassCleanup to run code after all tests in a class have run
    '<ClassCleanup()>  _
    'Public Shared Sub MyClassCleanup()
    'End Sub
    '
    'Use TestInitialize to run code before running each test
    '<TestInitialize()>  _
    'Public Sub MyTestInitialize()
    'End Sub
    '
    'Use TestCleanup to run code after each test has run
    '<TestCleanup()>  _
    'Public Sub MyTestCleanup()
    'End Sub
    '
#End Region

    Private mSimErr As SimErr.SimErr

    '''<summary>
    '''A test for SimErr
    '''</summary>
    <TestMethod()> _
    Public Sub SimErrTest()
        Dim filename As String = "teamjoe.log"
        mSimErr = New SimErr.SimErr(filename)
        Dim ans As Integer = Retry()
        Console.Write("Collatz conjecture at 500 satisfied after step ")
        Console.WriteLine(ans)

        mSimErr.SimDone()
        Assert.AreEqual(110, ans)
    End Sub

    Function Collatz(n As Integer)
        Dim cnt As Integer = 0

        If (mSimErr.SimError("Collatz", 8)) Then
            Return -1
        End If

        While (n > 1)
            cnt = cnt + 1

            If (n Mod 2 > 0) Then
                n = n * 3 + 1
            Else
                n = n / 2
            End If

        End While

        Return cnt
    End Function

    Function Retry() As Integer
        Dim ret As Integer = Collatz(500)

        If (mSimErr.SimError("Retry", 5)) Then
            Return -1
        End If

        Do While (ret < 0)
            mSimErr.SimFix("If at first you don't succeed, try again.")
            ret = Collatz(500)
        Loop

        Return ret
    End Function

End Class
