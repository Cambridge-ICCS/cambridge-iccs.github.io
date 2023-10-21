program typesTutorial
  implicit none

  ! Some examples of declaring variables with type signatures
  logical :: x = .true.
  logical :: y = .false.
  integer :: i = 0

  ! Array of flotating point
  real, dimension(10,20) :: matrix

  ! Derived data type examples
  type Coords
    real :: lat
    real :: lon
    real :: sigma
  end type Coords

  ! Declaring a variable using our new data type
  type(Coords) :: origin

  ! Using a derived data type
  origin%lat = "hello"
  origin%lon = 0.0
  origin%sigma = 0.0

  ! Example of casting
  i = int(0.1)
  write (*,*) i

  ! Unsafe cast (just copy the data)
  i = transfer(0.1, i)
  write (*,*) i

end program