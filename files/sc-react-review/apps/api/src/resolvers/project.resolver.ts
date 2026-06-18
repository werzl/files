@ObjectType()
export class User {
  @Field(() => ID)
  id: string;

  @Field()
  name: string;
}

@ObjectType()
export class Project {
  @Field(() => ID)
  id: string;

  @Field()
  name: string;

  @Field(() => ID)
  userId: string;

  @Field(() => User)
  user: User;
}

export const resolvers = {
  Query: {
    // Fetches list of projects
    projects: async (parent, args, context) => {
      return context.prisma.project.findMany();
    },
  },
  Project: {
    // Fetches the user for each project
    user: async (parent, args, context) => {
      // Assume context.prisma.user.findUnique is the DB call
      return context.prisma.user.findUnique({
        where: { id: parent.userId },
      });
    },
  },
};
