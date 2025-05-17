# test_lorenz.py
import unittest
from Lorenz import lorenz_step, simulate_lorenz


class TestLorenzAttractor(unittest.TestCase):
    def test_lorenz_step_typical(self):
        x, y, z = 1.0, 1.0, 1.0
        sigma, rho, beta, dt = 10.0, 28.0, 8.0 / 3.0, 0.01
        x1, y1, z1 = lorenz_step(x, y, z, sigma, rho, beta, dt)
        self.assertNotEqual((x, y, z), (x1, y1, z1),
                            "Values must change after one step")

    def test_lorenz_step_no_change_when_equal(self):
        # В особливих параметрах може не бути зміни
        x, y, z = 0.0, 0.0, 0.0
        sigma, rho, beta, dt = 10.0, 28.0, 8.0 / 3.0, 0.01
        x1, y1, z1 = lorenz_step(x, y, z, sigma, rho, beta, dt)
        self.assertAlmostEqual(x1, 0.0)
        self.assertAlmostEqual(y1, 0.0)
        self.assertAlmostEqual(z1, 0.0)

    def test_simulation_length(self):
        x0, y0, z0 = 1.0, 1.0, 1.0
        sigma, rho, beta, dt = 10.0, 28.0, 8.0 / 3.0, 0.01
        steps = 500
        xs, ys, zs = simulate_lorenz(x0, y0, z0, sigma, rho, beta, dt, steps)
        self.assertEqual(len(xs), steps)
        self.assertEqual(len(ys), steps)
        self.assertEqual(len(zs), steps)


if __name__ == '__main__':
    unittest.main()
