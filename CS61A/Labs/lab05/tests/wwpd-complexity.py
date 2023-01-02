test = {
  'name': 'Orders of Growth',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '507089800ba7da0a1bf17af624b88bf9',
          'choices': [
            'Logarithmic - Θ(log(n))',
            'Linear - Θ(n)',
            'Quadratic - Θ(n^2)',
            'Exponential - Θ(2^n)'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          What is the order of growth of `is_prime` in terms of `n`?
          
          def is_prime(n):
              for i in range(2, n):
                  if n % i == 0:
                      return False
              return True
          """
        },
        {
          'answer': '0794d0e28ff429a96c593376012236a7',
          'choices': [
            'Logarithmic - Θ(log(n))',
            'Linear - Θ(n)',
            'Quadratic - Θ(n^2)',
            'Exponential - Θ(2^n)'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          What is the order of growth of `bar` in terms of `n`?
          
          def bar(n):
              i, sum = 1, 0
              while i <= n:
                  sum += biz(n)
                  i += 1
              return sum
          
          def biz(n):
              i, sum = 1, 0
              while i <= n:
                  sum += i**3
                  i += 1
              return sum
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
