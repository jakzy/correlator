import cv2
from matplotlib import pyplot as plt


class Correlator():
    methods = {'CCOEFF': cv2.TM_CCOEFF,
               'CCOEFF_NORMED': cv2.TM_CCOEFF_NORMED,
               'CCORR': cv2.TM_CCORR,
               'CCORR_NORMED': cv2.TM_CCORR_NORMED,
               'SQDIFF': cv2.TM_SQDIFF,
               'SQDIFF_NORMED': cv2.TM_SQDIFF_NORMED}
    colors = {'red': (0, 0, 255),
              'orange': (0, 140, 255),
              'yellow': (0, 255, 255),
              'green': (0, 255, 0),
              'blue': (255, 0, 0),
              'purple': (211, 0, 148),
              'black': (0, 0, 0),
              'white': (255, 255, 255)}

    color = colors['red']
    is_full = False
    is_part = False
    loc = 'min'
    method = methods['SQDIFF']

    mp_fl = False

    def set_full(self, path):
        self.is_full = True
        self.img_rgb = cv2.imread(path)
        self.img_gray = cv2.cvtColor(self.img_rgb, cv2.COLOR_BGR2GRAY)

    def set_part(self, path):
        self.is_part = True
        self.template = cv2.imread(path, flags=cv2.IMREAD_ANYDEPTH)
        self.h, self.w = self.template.shape[::]

    def set_method(self, meth):
        if meth in self.methods:
            self.method = self.methods[meth]
            if meth in ['SQDIFF', 'SQDIFF_NORMED']:
                self.loc = 'min'
            else:
                self.loc = 'max'
        else:
            print("Illegal method")
        return

    def match_img(self):
        self.res = cv2.matchTemplate(self.img_gray, self.template, self.method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(self.res)
        if self.loc == 'max':
            self.top_left = max_loc
        elif self.loc == 'min':
            self.top_left = min_loc
        self.bottom_right = (self.top_left[0] + self.w, self.top_left[1] + self.h)
        plt.imshow(self.res, cmap="inferno")
        if self.mp_fl:
            self.mp = 'test/buf_map' + str(self.method) + '.jpg'
            plt.imsave(self.mp, self.res, cmap="inferno")
            pic = cv2.imread(self.mp)
            cv2.imshow('Map of corr', pic)
            cv2.waitKey()
            cv2.destroyAllWindows()

    def repr_res(self, res=None):
        cv2.rectangle(img=self.img_rgb, pt1=self.top_left, pt2=self.bottom_right, color=self.color, thickness=2)
        cv2.imshow('Matched image', self.img_rgb)
        cv2.waitKey()
        cv2.destroyAllWindows()
        if res:
            cv2.imwrite(res, self.img_rgb)

    def set_color(self, color):
        if color in self.colors:
            self.color = self.colors[color]
        else:
            print("Illegal color")